package section4;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;

public class Polynomial {
	char name;
	public LinkedList<Term> terms;
	
	public Polynomial(char name) {
		this.name = name;
		terms = new LinkedList<Term>();
	}
	
	public void addTerm(int coef, int expo) {
		if (coef == 0) {
			return;
		}
		
		ListIterator<Term> iter = terms.listIterator();
		while (iter.hasNext()) {
			Term t = iter.next();
			if (t.expo == expo) {
				t.coef += coef;
				
				if (t.coef == 0) {
					iter.remove();
				}
				return;
			} else if (t.expo < expo) {
				iter.previous();
				iter.add(new Term(coef, expo));
				return;
			}
		}
		
		iter.add(new Term(coef, expo));
	}
	
	public int calc(int x) {
		int result = 0;
		
		Iterator<Term> iter = terms.iterator();
		
		while (iter.hasNext()) {
			Term t = iter.next();
			result += t.calc(x);
		}
		
		return result;
	}
	
	public String toString() {
		String result = "";
		
		Iterator<Term> iter = terms.iterator();
		while (iter.hasNext()) {
			Term t = iter.next();
			result += ("+" + t.toString());
		}
		
		return result;
		
	}
	
}
