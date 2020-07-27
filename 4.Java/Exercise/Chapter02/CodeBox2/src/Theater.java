public class Theater {
    private Seat[][] seats;

    private int rowCount, colCount;

    public Theater(int rowCount, int colCount) {
        if (rowCount > 26) {
            rowCount = 26; // number of alphabets
        }
        seats = new Seat[rowCount][colCount];
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                seats[i][j] = new Seat();
            }
        }

        this.rowCount = rowCount;
        this.colCount = colCount;
    }

    public boolean reserve(String name, char rowChar, int col, int numSeat) {
        int row = getRowIndex(rowChar);

        for (int i=0; i<numSeat; i++) {
            if (checkExistence(row, col-1+i) && !seats[row][col-1+i].isOccupied()) {

            } else {
                return false;
            }
        }

        for (int i=0; i<numSeat; i++) {
            seats[row][col-1+i].reserve(name);
        }

        return true;
    }

    public int cancel(String name) {
        int count = 0;
        for (int i=0; i<rowCount; i++) {
            for (int j=0; j<colCount; j++) {
                Seat seat = seats[i][j];
                if (seat.isOccupied() && seat.match(name)) {
                    count++;
                    seat.cancel();
                }
            }
        }

        return count;
    }

    public int cancel(char rowChar, int col, int numSeat) {
        int row = getRowIndex(rowChar);
        int count = 0;

        for (int i=0; i<numSeat; i++) {
            Seat seat = seats[row][col-1+i];
            if (seat.isOccupied()) {
                count++;
                seat.cancel();
            }
        }

        return count;
    }

    public int getNumberOfReservedSeat() {
        int count = 0;

        for (int i=0; i<rowCount; i++) {
            for (int j=0; j<colCount; j++) {
                Seat seat = seats[i][j];
                if (seat.isOccupied()) {
                    count++;
                }
            }
        }

        return count;
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

    private int getRowIndex(char uppercaseChar) {
        return uppercaseChar - 'A';
    }

    private boolean checkExistence(int row, int col) {
        if (row < 0 || row >= rowCount || col < 0 || col >= colCount) {
            return false;
        } else {
            return true;
        }
    }
}