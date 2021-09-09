package study.datajpa.repository;

import java.util.List;
import java.util.Optional;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Slice;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import study.datajpa.dto.MemberDto;
import study.datajpa.entity.Member;

public interface MemberRepository extends JpaRepository<Member, Long> {

  List<Member> findByUsernameAndAgeGreaterThan(String username, int age);

  List<Member> findHelloBy();

  List<Member> findTop3HelloBy();

  @Query("select m from Member m where m.username = :username and m.age = :age")
  List<Member> findUser(@Param("username") String username, @Param("age") int age);

  @Query("select m.username from Member m")
  List<String> findUsernameList();

  @Query("select new study.datajpa.dto.MemberDto(m.id, m.username, t.name) from Member m join m.team t")
  List<MemberDto> findMemberDto();

  @Query("select m from Member m where m.username in :names")
  List<Member> findByNames(@Param("names") List<String> names);

  List<Member> findListByUsername(String username);  // 컬렉션 반환 가능
  Member findMemberByUsername(String username);  // 단건 반환 가능
  Optional<Member> findOptionalByUsername(String username);  // 단건 Optional 반환 가능

  @Query(value = "select m from Member m left join m.team t", countQuery = "select count(m.username) from Member m")  // select 쿼리에 join이 많지만 count 쿼리에는 join이 필요 없는 경우 이렇게 설정해놓으면 된다.
  Page<Member> findByAge(int age, Pageable pageable);

  @Modifying(clearAutomatically = true)
  @Query("update Member m set m.age = m.age + 1 where m.age >= :age")
  int bulkAgePlus(@Param("age") int age);

}
