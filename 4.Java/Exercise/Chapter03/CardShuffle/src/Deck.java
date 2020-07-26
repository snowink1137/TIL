import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Deck {
    private ArrayList<Card> cards;

    public Deck() {
        cards = new ArrayList<Card>();
    }

    public void addCard(Card card) {
        cards.add(card);
    }

    public ArrayList<Card> getCards() {
        return cards;
    }

    public void print() {
        for (Card card : cards) {
            System.out.println(card.toString());
        }
    }

    public void shuffle() {
        Random random = new Random();
        for (int i=0; i<cards.size(); i++) {
            int temp = random.nextInt(cards.size());
            Collections.swap(cards, i, temp);
        }
    }

    public Deck deal(int count) {
        Deck hand = new Deck();
        if (count == 5) {
            for (int i=0; i<5; i++) {
                hand.addCard(cards.get(cards.size()-1));
                cards.remove(cards.size()-1);
            }
        }
        return hand;
    }
}