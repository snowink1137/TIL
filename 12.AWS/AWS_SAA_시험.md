> AWS SAA 시험을 준비하면서, 기억해둘 내용을 저장해 놓는 문서
>
> udemy 연습 테스트 활용



[TOC]





# 연습 테스트 1

- Amazon Elastic Load Balancer는 하나의 리전에서만 실행되도록 설계되었다
- 전송 중 S3 데이터 보호 암호화 방법
  - 서버 측 암호화
    - 데이터 센터의 디스크에  저장하기 전에 객체를 암호화하고 객체를 다운로드 할 때 해독을 위해 Amazon S3에 요청하는 방식
    - Amazon S3 관리형 키를 사용한 서버 측 암호화(SSE-S3)
      - AWS에서 주기적으로 바뀌는 마스터 키를 사용해서 암호화
    - AWS Key Management Service에 저장된 고객 마스터 키(CMK)를 사용한 서버 측 암호화(SSE-KMS)
      - SSE-S3와 비슷하지만 추가 비용이 들고 별도의 권한 설정이 필요함
      - 사용 주체를 표시하는 감사 추적 기능 등 추가 기능을 사용할 수 있음
    - 고객 제공 키를 사용한 서버 측 암호화(SSE-C)
  - 클라이언트 측 암호화
    - 클라이언트 측 데이터를 암호화하여 암호화된 데이터를 Amazon S3에 업로드. 이 경우 사용자가 암호화 프로세스, 키 및 관련 도구를 관리해야 하는 방식
    - AWS Key Management Service에 저장된 고객 마스터 키(CMK)를 사용
    - 애플리케이션 내에 저장한 마스터 키를 사용
      - 객체를 업로드 할 때 Amazon S3 암호화 클라이언트에 클라이언트 측 마스터 키를 제공한다. 그리고 업로드 할 때 이 키를 사용하고, 어떤 키를 사용했는지 설명하는 내용을 메타데이터에 남긴다
- 네트워크 ACL(액세스 제어 목록)
  - 네트워크 ACL(액세스 제어 목록)은 1개 이상의 서브넷 내부와 외부의 트래픽을 제어하기 위한 방화벽 역할을 하는 VPC를 위한 선택적 보안 계층입니다. 보안 그룹과 비슷한 규칙으로 네트워크 ACL을 설정하여 VPC에 보안 계층을 더 추가할 수 있습니다
  - VPC에 있는 각 서브넷을 네트워크 ACL과 연결해야 한다. 명시적으로 연결하지 않으면, 기본 네트워크 ACL에 자동 연결됨
  - 네트워크 ACL을 여러 서브넷과 연결할 수 있다. 하지만 서브넷은 한 번에 하나의 네트워크 ACL에만 연결할 수 있다
  - 네트워크 ACL에는 별개의 인바운드 및 아웃바운드 규칙이 있다. 각 규칙은 트래픽을 허용하거나 거부할 수 있다
  - 네트워크 ACL은 상태 비저장이다. 즉, 허용되는 인바운드 트래픽에 대한 응답이라도 아웃바운드 트래픽에 대한 규칙을 따른다
  - 네트워크 ACL 규칙은 규칙 번호에 따라 가장 **낮은** 규칙에서 높은 규칙까지 평가되며 규칙이 적용되는 트래픽이 있으면 즉시 실행된다
- Amazon EBS 볼륨
  - 인스턴스의 수명과는 독립적으로 유지될 수 있는 오프인스턴스 스토리지이다
  - 프로덕션 중에 실시간 구성 변경을 지원한다. 볼륨 유형, 크기, IOPS 용량 수정 가능
- CIDR 블록
  - 주소 자체를 의미하려면 xxx.xxx.xxx.xxx/32 로 해야함. xxx.xxx.xxx.xxx/0 으로 하면 안됨. 이거는 전체 네트워크를 의미한다고 함
  - 출처
    - https://seogineer.tistory.com/87
- AWS CloudWatch는 AWS 리소스를 위한 모니터링 도구이고, AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사, 위험 감사를 지원하는 서비스이다. 이 과정에서 CloudWatch Logs와 통합해서 사용할 수 있다
- RAID 0 vs RAID 1
  - ![RAID 0 vs RAID 1](AWS_SAA_시험.assets/raid-0-vs-raid-1-thumbnail.jpg)
  - 따라서 읽기/쓰기 속도를 높이려면 RAID 0이 낫다
  - 출처
    - https://www.partitionwizard.com/partitionmanager/raid-0-vs-raid-1.html
- ACL vs 보안 그룹
  - ![         트래픽은 보안 그룹과 네트워크 ACL을 통해 제어됨       ](AWS_SAA_시험.assets/security-diagram.png)
  - 출처
    - https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_Security.html
- AWS Snow Family
  - ![AWS Snow Family](AWS_SAA_시험.assets/aws-snow-family-snowcone-snowball-snowmobile.png)
  - AWS Snow Family는 까다로운 비데이터 센터 환경 및 네트워크 연결이 일관되지 않은 위치에서 작업을 실행해야하는 고객을 지원한다
  - AWS와 일관된 엣지 컴퓨팅 디바이스
    - 네트워크 연결 없이도 직접 애플리케이션을 실행한다
    - 엣지에서 데이터를 처리하고 AWS로 데이터를 마이그레이션한다
  - snowcone < snowball < snowmobile
  - snowball에서 Glacier로 데이터를 직접 이동할 수는 없다. 먼저 S3를 거친 후 Glacier로 보내야 한다
- 

