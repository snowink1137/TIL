public class GradeCalculator {
    public String name;
    public double latestGPA;
    public int totalCredit;
    public double thisTotalGPA;
    public int thisTotalCredit;
    public double thisTotalGrade;

    public GradeCalculator(String name, double latestGPA, int totalCredit) {
        this.name = name;
        this.latestGPA = latestGPA;
        this.totalCredit = totalCredit;
        this.thisTotalCredit = 0;
        this.thisTotalGrade = 0;
    }

    public void addCourse(Course course) {
        this.thisTotalGrade += course.grade * course.credit;
        this.thisTotalCredit += course.credit;
        this.thisTotalGPA = this.thisTotalGrade / this.thisTotalCredit;
    }

    public void print() {
        System.out.println("직전 학기 성적: " + latestGPA + " (총 " + totalCredit + "학점)");

        System.out.println("이번 학기 성적: " + thisTotalGPA + " (총 " + thisTotalCredit + "학점)");

        System.out.println("전체 예상 학점: " + (latestGPA*totalCredit+thisTotalGrade)/(totalCredit+thisTotalCredit) + " (총 " + (totalCredit+thisTotalCredit) + "학점)");
    }
}
