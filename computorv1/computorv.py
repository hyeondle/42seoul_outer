import sys
import re
import argparse
from collections import defaultdict
import cmath  # 복소수 계산

# 데이터를 읽고 분할하는 함수
def read_and_split_input(equation):
    data = equation.replace(" ", "").split('=')
    return data

# 항목을 추출하는 함수
def extract_terms(expression):
    return re.findall(r'[+-]?\d*\.?\d+(?:\*X\^\d+)?', expression)

# 항목을 지수승으로 정렬하는 함수
def sort_by_exponent(terms):
    return sorted(terms, key=lambda term: int(re.search(r'\^(\d+)', term).group(1)) if '*X^' in term else 0)

# 항목을 계수와 지수로 파싱하는 함수
def parse_term(term):
    if '*X^' in term:
        match = re.match(r'([+-]?\d*\.?\d+)\*X\^(\d+)', term)
        return float(match.group(1)), int(match.group(2))
    else:
        return float(term), 0

# 좌변과 우변의 항목을 처리하는 함수
def process_sides(left, right):
    terms = defaultdict(float)
    for term in left:
        coef, exp = parse_term(term)
        terms[exp] += coef
    for term in right:
        coef, exp = parse_term(term)
        terms[exp] -= coef
    return terms

# 모든 지수를 포함하도록 terms를 보정하는 함수
def complete_terms(terms):
    max_exp = max(terms.keys(), default=0)
    for exp in range(max_exp + 1):
        if exp not in terms:
            terms[exp] = 0.0
    return terms

# Reduced form을 생성하는 함수
def generate_reduced_form(terms):
    reduced_terms = []
    for exp in sorted(terms.keys()):
        coef = terms[exp]
        term = f'{coef:+.1f} * X^{exp}'
        reduced_terms.append(term)
    if reduced_terms:
        reduced_terms[0] = reduced_terms[0].lstrip('+')
    reduced_form = "Reduced form: " + " ".join(reduced_terms) + " = 0"
    reduced_form = reduced_form.replace(" +", " + ").replace(" -", " - ").replace(".0", "")
    return reduced_form

# 차수를 계산하는 함수
def calculate_degree(terms):
    return max(terms.keys(), default=0)

# 방정식을 푸는 함수
def solve_equation(degree, terms):
    if degree == 0:
        if terms[0] == 0:
            return "All real numbers are solutions."
        else:
            return "No solution exists."
    elif degree == 1:
        a = terms[1]
        b = terms[0]
        if a != 0:
            solution = -b / a
            return f"The solution is:\n{solution}"
        else:
            return "No solution exists."
    elif degree == 2:
        a = terms[2]
        b = terms[1]
        c = terms[0]
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            return f"Discriminant is strictly positive, the two solutions are:\n{root1.real}\n{root2.real}"
        elif discriminant == 0:
            root = -b / (2*a)
            return f"Discriminant is zero, the solution is:\n{root}"
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            return f"Discriminant is strictly negative, the two solutions are:\n{root1}\n{root2}"
    else:
        return "The polynomial degree is strictly greater than 2, I can't solve."

# 메인 함수
def main():
    parser = argparse.ArgumentParser(description='Process a polynomial equation.')
    parser.add_argument('equation', type=str, help='The polynomial equation to solve')
    args = parser.parse_args()

    data = read_and_split_input(args.equation)
    left = extract_terms(data[0])
    right = extract_terms(data[1])
    
    left_sorted = sort_by_exponent(left)
    right_sorted = sort_by_exponent(right)
    
    terms = process_sides(left_sorted, right_sorted)
    terms = complete_terms(terms)
    
    reduced_form = generate_reduced_form(terms)
    print(reduced_form)
    
    degree = calculate_degree(terms)
    print(f"Polynomial degree: {degree}")
    
    solution = solve_equation(degree, terms)
    print(solution.replace(".0", ""))

if __name__ == "__main__":
    main()
