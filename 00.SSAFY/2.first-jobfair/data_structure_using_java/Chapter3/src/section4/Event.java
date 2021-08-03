package section4;

public abstract class Event implements Comparable {
	public String title;
	
	public Event(String title) {
		this.title = title;
	}
	
	public abstract boolean isRelevant(MyDate date);
	public abstract MyDate getRepresentiveDate();
	
	public int compareTo(Object other) {
		MyDate mine = getRepresentiveDate();
		MyDate yours = ((Event) other).getRepresentiveDate();
		
		return mine.compareTo(yours);
	}
}
