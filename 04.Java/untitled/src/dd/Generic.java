package dd;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class SoltClass <E extends Comparable<? super E>>{
}

class SoltClass2 <E extends Comparable<E>>{
}
class Person {
}
class Student extends Person implements Comparable<Person>{

  int age;

  @Override
  public int compareTo(Person person) {
    return 1;
  }
}

class Student2 extends Person implements Comparable<Student2>{

  int age;

  @Override
  public int compareTo(Student2 s) {
    return 1;
  }
}

public class Generic {


  public static void main(String[] args) {
    SoltClass<Student> s = new SoltClass<Student>();
    SoltClass2<Student2> s2 = new SoltClass2<Student2>();

    List<String> arr = new LinkedList<String>();
  }
}