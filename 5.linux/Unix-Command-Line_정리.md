# 유닉스 커맨드 라인 정리

> codeit 유닉스 커맨드 라인 강의 중 나중에 다시 볼 내용을 정리  
> https://www.codeit.kr/courses/unix-command-line

[TOC]



## 1. 유닉스 커맨드 배우기

### CLI 환경과 유닉스

- 개발자로서 일하기 위해서는 Linux, ubuntu, Red Hat, Chrome OS 등의 운영체제를 다룰 줄 알아야 한다. 모든 것을 알 필요는 없지만 최소한 명령어는 다룰 줄 알아야 한다. 다행히(?)도 윈도우를 제외한 많은 운영체제가 UNIX 계열 운영체제(UNIX라는 뿌리를 가진)이기 때문에, UNIX 커맨드를 배우면 여러 운영체제를 어느정도 다룰 수 있다
- 보통 운영체제에는 1000개 이상의 command가 있지만, 20~30 command만 알아도 업무에 지장이 없다고 한다
- Unix
  - 1970년대 초 미국 벨 연구소에서 켄 톰슨과 데니스 리치의 주도로 개발된 운영체제
  - 대부분 C언어로 작성되었기 때문에 다른 컴퓨터에 수정해서 적용하기 쉬웠음
    - 따라서 다양한 Unix가 생길 수 있었다
    - POSIX: Unix라면 갖춰야 할 규격과 기능을 정의한 표준
  - 벨 연구소는 AT&T 소속이었기 때문에 Unix를 사용하거나 수정하려면 라이센스 비용이 발생했다
- GNU/Linux
  - 자유 소프트웨어 재단(Free Software Foundation)에서 Unix의 코드를 한 줄도 사용하지 않고 Unix와 유사한 운영 체제를 만들고자 GNU 프로젝트를 시작하였다. GNU는 "GNU is Not Unix"라는 재귀적인 의미를 담고 있다
  - 하지만 GNU는 운영체제의 핵심 부분인 Kernel이 Unix에 비해 부족하다는 어려움을 겪고 있었다. 이 때, Linus Torvalds라는 핀란드 대학생이 UNIX의 교육용 버전인 MINIX에서 아이디어를 얻어 새로운 커널을 만들었고 이를 Linux Kernel이라는 이름으로 공개했다
  - GNU 프로젝트에서는 이 커널을 가져다 쓰기로 했고 결국 GNU 운영 체제가 완성되었다. Linux Kernel을 사용했기 때문에, 운영체제의 이름은 GNU/Linux가 되었다 
  - 원래 제대로 얘기하려면 Linux는 Linux Kernel만들 얘기하는 것이고 운영체제의 정확한 이름은 GNU/Linux가 맞다. 하지만 그냥 Linux라고 하는 경우가 많다
  - 원래 인기가 많던 UNIX의 편의성에, 무료로 사용할 수 있어서 반응이 좋았다
  - GNU/Linux를 변형해서 ubuntu, Red Hat, CentOS, debian 등의 운영체제가 만들어 졌으며 이를 리눅스 배포판이라고 한다
  - 이러한 GNU/Linux들도 유닉스 표준인 POSIX를 사실상 대부분 만족하도록 만들어져 있다
  - Unix-certified vs Unix-like
    - POSIX 인증을 받으면 Unix-certified가 되는 것이고 인증 없이 비슷한 경우 Unix-like라고 한다
    - HP unix, AIX, macOS 등은 인증을 받은 정식 Unix이고, ubuntu, Red Hat, CentOS, debian 등은 Unix-like이다
    - POSIX를 모두 만족하지만 라이센스 비용때문에 인증을 안받는 경우도 있다
- GUI(Graphical User Interface) vs CLI(Command Line Interface)
  - CLI의 장점
    1. 성능
       - 정보를 표현할 때 그래픽 작업이 없기 때문에 성능이 좋다
    2. 명확성
       - 마우스로 많은 단계를 거치다보면 실수할 가능성이 높다
       - 커맨드를 한번 만들어 놓고 복사해서 사용하면 실수할 가능성이 적고 많은 과정을 한 번의 커맨드로 요약할 수 있기 때문에 명확하다. 따라서 처음에 익숙해지기 어려울 수 있지만 한번 익숙해지면 오히려 컴퓨터를 단순하고 정확하게 사용할 수 있다
- 

