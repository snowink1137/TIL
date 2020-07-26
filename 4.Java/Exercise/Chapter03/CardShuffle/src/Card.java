public class Card {
    public final int suitNumber;
    public final int rankNumber;

    public Card(int suitNumber, int rankNumber) {
        this.suitNumber = suitNumber;
        this.rankNumber = rankNumber;
    }

    public String getSuit() {
        if (suitNumber == 1) {
            return "Clubs";
        } else if (suitNumber == 2) {
            return "Hearts";
        } else if (suitNumber == 3) {
            return "Diamonds";
        } else if (suitNumber == 4) {
            return "Spades";
        } else {
            return null;
        }
    }

    public String getRank() {
        if (rankNumber == 1) {
            return "Ace";
        } else if (rankNumber == 11) {
            return "Jack";
        } else if (rankNumber == 12) {
            return "Queen";
        } else if (rankNumber == 13) {
            return "King";
        } else {
            return Integer.toString(rankNumber);
        }
    }

    public String toString() {
        return getRank() + " of " + getSuit();
    }
}
