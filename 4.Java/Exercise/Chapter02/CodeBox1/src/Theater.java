public class Theater {
    private Seat[][] seats;
    private int rowCount, colCount;

    public Theater(int rowCount, int colCount) {
        this.rowCount = rowCount;
        this.colCount = colCount;
        seats = new Seat[rowCount][colCount];

        for (int i=0; i<rowCount; i++) {
            for (int j=0; j<colCount; j++) {
                seats[i][j] = new Seat();
            }
        }
    }

    public void printSeatMatrix() {
        System.out.print("  ");
        for (int i = 1; i <= 9; i++) {
            System.out.print("  " + i);
        }
        System.out.println();

        for (int i = 0; i < rowCount; i++) {
            System.out.print((char) ('A' + i) + ": ");
            for (int j = 0; j < colCount; j++) {
                Seat s = seats[i][j];
                if (s.isOccupied()) {
                    System.out.print("[O]");
                } else {
                    System.out.print("[ ]");
                }
            }
            System.out.println();
        }
    }
}