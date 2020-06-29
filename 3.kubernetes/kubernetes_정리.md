# kubernetes 정리

- inflearn [대세는 쿠버네티스] 강의 메모
- 참조: https://kubetm.github.io/practice/  
  위에 올려진 강의 노트를 간단하게 훑어볼때 쓰기위해 정리함



## Introduction

- 큰 기업들은 대규모의 서비스를 운영하고 있고 있기 때문에 최대한 자원을 효율적으로 쓰고, 운영 환경을 자동화하고 싶어한다.  
  그래서 가상화 기술과 이를 자동 운영하는 오케스트레이터 기술의 발전이 이루어졌다
- ![image-20200627193727776](kubernetes_정리.assets/image-20200627193727776.png)



## [기초편] 기초 다지기

### 1. Why Kubernetes?

- 서버 자원을 효율적으로 사용할 수 있다
  - 예를 들어 전통적인 방식에서 3가지 시스템이 있다면, 각 시스템 별로 3대씩 서버를 미리 준비해놓아야 한다. 하지만 3가지 시스템의 트래픽이 몰리는 시간이 다르다면? 많은 서버는 그 시간 동안 자원을 낭비하는 셈이 된다.  
    쿠버네티스는 이러한 낭비를 Auto scaling, Auto Healing(장애 복구), Deployment(Rolling Update, ReCreate) 등의 기능으로 줄여준다



### 2. VM vs Container

- ![image-20200627195807357](kubernetes_정리.assets/image-20200627195807357.png)
- ![image-20200627195731232](kubernetes_정리.assets/image-20200627195731232.png)
- Container는 리눅스 가상화 기술인 namespace와 cgroups를 이용한다. 이를 사용하여 여러 컨테이너들이 호스트 자원을 나눠쓰게 한다(격리).  
  namespace는 커널 영역(mnt, pid, net, ipc, uts, user)을 나눠서 쓰게 해주고, cgroups는 자원 영역(memory, CPU, I/O, network)을 나눠서 쓰게 해준다



### 3. Getting started - Kubernetes

- ![image-20200627200131864](kubernetes_정리.assets/image-20200627200131864.png)



### 4. Kubernetes Overview

- ![image-20200627201325570](kubernetes_정리.assets/image-20200627201325570.png)



### 0. 쿠버네티스 설치

- 세 가지 Usecase  
  ![image-20200627202912481](kubernetes_정리.assets/image-20200627202912481.png)

- Usecase1[베어메탈]  
  ![image-20200627203756426](kubernetes_정리.assets/image-20200627203756426.png)  
  https://kubetm.github.io/practice/appendix/installation_case1/
- Usecase2[내 PC + VirtualBox]  
  ![image-20200627203639743](kubernetes_정리.assets/image-20200627203639743.png)  
  https://kubetm.github.io/practice/appendix/installation_case2/



### 5. Object - Pod

- ![image-20200627205101082](kubernetes_정리.assets/image-20200627205101082.png)



### 5. Object - Service

- ![image-20200627213742737](kubernetes_정리.assets/image-20200627213742737.png)



### 5. Object - Volume

- ![image-20200627215924050](kubernetes_정리.assets/image-20200627215924050.png)



### 5. Object - ConfigMap, Secret

- ![image-20200628193913186](kubernetes_정리.assets/image-20200628193913186.png)
  - 유저, SSH, Key 값 정보 등은 환경에 따라 바뀌어야 한다. 각 Container 이미지를 따로 만들어서 보관하기에는 자원의 낭비가 크므로, 해당 정보들을 따로 관리해주는 Object가 ConfigMap, Secret이다. Container는 해당 정보를 비운 채로 보관하고, ConfigMap과 Secret Object를 연결해서 사용하는 방식으로 Container를 사용한다
- ![image-20200628194830289](kubernetes_정리.assets/image-20200628194830289.png)
  - Env(Literal) 방식은 정보를 메모리에 저장한다. 따라서 성능에 영향을 줄 수 있다
  - Env(File) 방식과 Volume Mount(File) 방식은 둘 다 파일을 사용하지만, Env(File) 방식은 Pod에 정보를 한번 주입하면 끝이다. 파일이 업데이트 되어도 Pod에 업데이트 안됨
  - cf) Base64: 64진법 인코딩 방식



### 5. Object - Namespace, ResourceQuota, LimitRange

- ![image-20200628200150658](kubernetes_정리.assets/image-20200628200150658.png)
  - Pod를 Namespace라는 논리적 개념으로 묶는다. 여기에 Resource Quota라는 리소스 관리 Object를 붙이고, LimitRange라는 Object를 붙여서 Namespace로 들어올 수 있는 Pod에 제한을 둔다. Resource Quota와 Limit Range는 Namespace 뿐만 아니라 Kubernetes Cluster에도 붙여서 전체 자원에 대한 관리도 가능하다
- ![image-20200628200924631](kubernetes_정리.assets/image-20200628200924631.png)
  - 하나의 Namespace에는 Pod의 이름이 중복될 수 없다. 다른 Namespace에서 Object들이 name으로 통신할 수 없다. IP를 사용하면 가능하다. Namespace들이 공통으로 사용하는 PV, Node와 같은 것들도 있다. ResourceQuota와 LimitRange에 request, limits, min, max 등의 옵션을 주어서 해당 옵션을 모두 만족해야만 해당 Namespace가 관리하는 Pod를 생성할 수 있다
  - Service Object 역시 NodePort를 사용할 때, 같은 Namespace에서 다른 Service Object가 같은 port를 사용할 수 없다



### 6. Controller - 개요

- Controller의 역할  
  ![image-20200628212150356](kubernetes_정리.assets/image-20200628212150356.png)
  - 위와 같은 역할을 ReplicationController, ReplicaSet, HPA, Deployment, CronJob 등의 Object가 수행한다



### 6. Controller - Replication Controller, ReplicaSet

- ![image-20200628213039741](kubernetes_정리.assets/image-20200628213039741.png)
  - Replication Controller는 Deprecated됨. Template, Replicas 기능은 Replication Controller와 ReplicaSet 모두 가지고 있고, Selector 기능은 ReplicaSet에만 있음
  - Replicas 기능에 갯수를 지정하고, Templete Pod를 지정하면 Pod를 자동으로 생성하므로, Pod를 직접 생성하지 않고, Controller만 만드는 방식으로 많이 사용한다
    - Controller를 삭제하면 보통 해당 Pod들도 사라지는데, kubectl 명령으로 Controller만 삭제하는 기능도 있다



### 6. Controller - Deployment

- ![image-20200628214505068](kubernetes_정리.assets/image-20200628214505068.png)
  - 네 가지의 배포 방식이 있다. 방식에 따라 자원 효율적이거나, Downtime이 없거나, test를 해보며 배포하거나(Canary) 할 수 있다
  - ReCreate와 Rolling Update 방식은 Deployment Object를 조정해서 업데이트한다. Blue/Green 방식과 Canary 방식은 Deployment를 조정해서 업데이트하는 것이 아니다(Blue/Green 방식의 경우, Service Object의 `ver` 라벨을 직접 조정해서 업데이트한다)
- ![image-20200628215107870](kubernetes_정리.assets/image-20200628215107870.png)
  - Deployment Object가 replicaSet의 replicas를 조정해서 업데이트를 실행한다. ReCreate 방식은 이 숫자를 한번에 0으로 바꾸는 방식이고, Rolling Update 방식은 일정 간격을 두고 숫자를 조정하는 방식이다
  - revisionHistoryLimit 라는 옵션을 이용해서, ReplicaSet의 history 갯수를 지정해서 롤백하는 경우에 기존 ReplicaSet을 사용할 수 있도록 한다



### 6. Controller - DaemonSet, Job, CronJob

- ![image-20200629211935120](kubernetes_정리.assets/image-20200629211935120.png)
  - DaemonSet은 Node의 현재 자원 상태에 따라 Pod를 배분하는 것이 아니고, Node 별로 Pod을 하나씩 두고 쓴다. Performance, Logging, Storage 등 필수적으로 쓰는 Pod를 생성하기 때문이다
  - CronJob은 Job을 관리하는 Object이다. Job은 Pod를 만들어서 Job을 수행한다. ReplicaSet과 Job의 차이는 Pod에 문제가 생겼을 때 나타난다. ReplicaSet은 Restart를 수행하고, Job은 그냥 해당 Pod를 Finish한다. Finish해도 해당 Pod가 없어지는 것은 아니고, 자원을 사용하지 않는 상태가 되므로, 해당 Pod에 접속해서 로그를 확인할 수 있다
- ![image-20200629212920213](kubernetes_정리.assets/image-20200629212920213.png)