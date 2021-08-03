public class Course {
    public static final int CREDIT_MAJOR = 3;
    public static final int CREDIT_GENERAL = 2;
    public String subject;
    public int credit;
    public double grade;

    public Course(String subject, int credit, String grade) {
        this.subject = subject;
        this.credit = credit;

        switch (grade) {
            case "A+":
                this.grade = 4.5;
                break;
            case "A":
                this.grade = 4.0;
                break;
            case "B+":
                this.grade = 3.5;
                break;
            case "B":
                this.grade = 3.0;
                break;
            case "C+":
                this.grade = 2.5;
                break;
            case "C":
                this.grade = 2.0;
                break;
            case "D+":
                this.grade = 1.5;
                break;
            case "D":
                this.grade = 1.0;
                break;
            case "F":
                this.grade = 0.0;
                break;
        }

    }
}
