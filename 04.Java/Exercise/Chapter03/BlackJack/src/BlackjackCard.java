public class BlackjackCard extends Card{
    public BlackjackCard(int suitNumber, int rankNumber) {
        super(suitNumber, rankNumber);
    }

    public int getValue() {
        String value = getRank();
        switch (value) {
            case "Ace":
                return 11;
            case "Jack":
            case "Queen":
            case "King":
                return 10;
            default:
                return Integer.parseInt(value);
        }
    }

    public boolean isAce() {
        String value = getRank();
        return value.equals("Ace");
    }
}
