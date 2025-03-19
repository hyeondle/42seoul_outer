/scop_vulkan_project
├── src/
│   ├── main.cpp         # 메인 진입점
│   ├── VulkanApp.cpp    # Vulkan 초기화 및 렌더링 루프
│   ├── Renderer.cpp     # Vulkan 렌더링 파이프라인
│   ├── ObjLoader.cpp    # .obj 파일 로더
│   ├── MathUtils.cpp    # 행렬 및 벡터 연산 (GLM 없이 직접 구현)
│   ├── Shader.cpp       # 셰이더 로딩 및 설정
│   ├── Texture.cpp      # 텍스처 로딩 및 적용
│   ├── InputHandler.cpp # 입력 처리 (키보드, 마우스)
│   ├── Makefile         # 빌드 시스템
│   └── shaders/
│       ├── vertex_shader.glsl
│       ├── fragment_shader.glsl
└── assets/
    ├── model.obj      # 기본 3D 객체
    ├── texture.png    # 텍스처 파일
