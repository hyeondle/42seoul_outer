#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <netinet/ip_icmp.h>
#include <time.h>
#include <fcntl.h>
#include <signal.h>
#include <time.h>
#include <sys/time.h>


#define RECV_TIMEOUT 1
#define PING_PKT_S 64
#define PORT_NO 0
#define PING_SLEEP_RATE 1000000

int pingloop = 1;

struct ping_pkt {
	struct icmp hdr;
	char msg[PING_PKT_S - sizeof(struct icmp)];
};

void int_handler(int temp)
{
	pingloop = 0;
}

char *dns_lookup(const char* hostname, struct sockaddr_in *address) {
	struct addrinfo hints, *res;
	int status;
	char ipstr[INET6_ADDRSTRLEN];
	char *ip = (char *)malloc(NI_MAXHOST * sizeof(char));
	void *addr;
	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_UNSPEC; // AF_INET or AF_INET6 to force version
	hints.ai_socktype = SOCK_STREAM;

	if ((status = getaddrinfo(hostname, NULL, &hints, &res)) != 0) {
		fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
		return NULL;
	}

	if (res->ai_family == AF_INET) { // IPv4
		struct sockaddr_in *ipv4 = (struct sockaddr_in *)res->ai_addr;
		addr = &(ipv4->sin_addr);
	} else { // IPv6
		struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)res->ai_addr;
		addr = &(ipv6->sin6_addr);
	}

	inet_ntop(res->ai_family, addr, ipstr, sizeof ipstr);

	strcpy(ip, ipstr);


	// for socket connection. need to modifiy some values
	(*address).sin_family = res->ai_family;
	(*address).sin_port = htons(0);
	(*address).sin_addr.s_addr = inet_addr(ip);

	freeaddrinfo(res); // free the linked list

	return ip; //need to free after use
}

/*

gethostbyname is now allowed function.
and it would not support ipv6

char*	dns_lookup(char* addr_host, struct sockaddr_in *address)
{
	struct hostent *host_entity;
	char *ip = (char *)malloc(NI_MAXHOST * sizeof(char));
	int i;

	if ((host_entity = gethostbyname(addr_host)) == NULL) {
		return NULL;
	}

	strcpy(ip, inet_ntoa(*(struct in_addr *)host_entity->h_addr_list[0]));

	(*address).sin_family = host_entity->h_addrtype;
	(*address).sin_port = htons(0);
	(*address).sin_addr.s_addr = *(long*)host_entity->h_addr_list[0];

	return ip;
}

*/

void send_ping(int ping_socketfd, struct sockaddr_in *ping_addr, char *ping_domain, char *ping_ip)
{
	int time_to_live = 64;
	int msg_count = 0;
	int i, addr_len, flag = 1;
	int msg_reveiced_count = 0;

	char rbuffer[128];
	struct ping_pkt* r_pckt;

	struct ping_pkt pckt;
	struct sockaddr_in r_addr;
	struct timespec time_start, time_end, tfs, tfe;
	long double rtt_msec = 0, total_msec = 0;
	struct timeval tv_out;
	tv_out.tv_sec = RECV_TIMEOUT;
	tv_out.tv_usec = 0;

	clock_gettime(CLOCK_MONOTONIC, &tfs);

	if (setsockopt(ping_socketfd, SOL_SOCKET, IP_TTL, &time_to_live, sizeof(time_to_live)) != 0)
	{
		printf("\nSetting socket options to TTL failed!\n");
		return;
	}
	else
	{
		printf("\nSocket set to TTL..\n");
	}

	setsockopt(ping_socketfd, SOL_SOCKET, SO_RCVTIMEO, (const char*)&tv_out, sizeof tv_out);

	while (pingloop) {
		flag = 1;
		bzero( &pckt, sizeof(pckt));

		pckt.hdr.type = ICMP_ECHO;
		pckt.hdr.un.echo.id = getpid();
		
	}
}

int main(int argc, char* argv[])
{
	int socket_fd;
	char *ip_address;
	struct sockaddr_in address;
	int address_length = sizeof(address);
	char buffer[NI_MAXHOST];

	if (argc != 2) {
		printf("\nUsage: \n"); // make usage
		return 0;
	}

	ip_address = dns_lookup(argv[1], &address);
	if (ip_address == NULL) {
		printf("\nDNS lookup failed! Could not resolve hostname!\n");
		return 0;
	}

	printf("ip : %s\n", ip_address);

	socket_fd = socket(AF_INET, SOCK_STREAM, 0);
	if (socket_fd < 0) {
		printf("\nSocket file descriptor not received!\n");
		return 0;
	}
	else
		printf("\nSocket file descriptor %d received\n", socket_fd);

	signal(SIGINT, int_handler); // catching interrupt

	send_ping(socket_fd, &address, ip_address, ip_address);
	// printf("ip : %s\n", ip_address);

	return 0;
}