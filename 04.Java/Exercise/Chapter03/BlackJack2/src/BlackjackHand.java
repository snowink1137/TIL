import java.util.ArrayList;

public class BlackjackHand extends Deck {
    private int ace = 0;

    public int getValue() {
        int tempTotal = 0;
        ArrayList<Card> cards = getCards();
        for (Card card : cards) {
            if (card.getRank().equals("Ace")) {
                ace++;
            } else {
                if (card.rankNumber > 10) {
                    tempTotal += 10;
                } else {
                    tempTotal += card.rankNumber;
                }
            }
        }

        while (ace > 0) {
            if (tempTotal + 11 > 21) {
                tempTotal += 1;
            } else {
                tempTotal += 11;
            }
            ace--;
        }

        return tempTotal;
    }

    public boolean isBusted() {
        if (getValue() > 21) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isBlackjack() {
        if (getValue() == 21 && getCards().size() == 2) {
            return true;
        } else {
            return false;
        }
    }
}
