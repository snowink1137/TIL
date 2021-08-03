package section3;

import java.util.Iterator;

public class Polynomial {
	char name;
	public MySingleLinkedList<Term> terms;
	
	public Polynomial(char name) {
		this.name = name;
		terms = new MySingleLinkedList<Term>();
	}
	
	public void addTerm(int coef, int expo) {
		if (coef == 0) {
			return;
		}
		
		Iterator<Term> p = terms.iterator();
		Iterator<Term> q = terms.iterator();
		
		Term t = null;
		int index = 0;
		
		while (p.hasNext()) {
			if (q == null) {
				q = terms.iterator();
			} else {
				q.next();
			}
			
			t = p.next();
			
			index++;
			
			if (t.expo <= expo) {
				break;
			}
			
			if (t != null && t.expo == expo) {
				t.coef += coef;
				
				if (t.coef == 0) {
					terms.remove(index);
				}
			} else {
				Term term = new Term(coef, expo);
				terms.add(index, term);
				
			}
			
		}
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
