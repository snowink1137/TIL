package section5;

import java.util.*;

public class Scheduler {

//	private int capacity = 10;
	public ArrayList<Event> events = new ArrayList<>();
//	public Event events [] = new Event [capacity];
//	public int n = 0;
	private Scanner kb;

	public void processCommand() {
		kb = new Scanner (System.in);
		while(true) {
			System.out.print("$ ");
			String command = kb.next();
			if (command.equals("addevent")){
				String type = kb.next();
				if (type.equalsIgnoreCase("oneday")) {
					handleAddOneDayEvent();
				} else if (type.equalsIgnoreCase("duration")) {
					handleAddDurationEvent();
				} else if (type.equalsIgnoreCase("deadline")) {
					handleAddDeadlinedEvent();
				}
			} else if (command.equals("list")) {
				handleList();
			} else if (command.equals("show")) {
				handleShow();
			} else if (command.equals("sort")) {
				Collections.sort(events);
			} else if (command.equals("exit")) {
				break;
			} 
		}

		kb.close();
	}

	private void handleShow() {
		String dateString = kb.next();
		MyDate theDate = parseDateString(dateString);
		
		for (Event ev : events) {
			// test if events[i] is relevant to the date, then print it;
			if (ev.isRelevant(theDate)) {
				System.out.println(ev.toString());
			}
		}
	}

	private void handleList() {
		for (Event ev : events) {  // enhanced for loop
			System.out.println("   "+ev.toString());
		}
	}

	private void handleAddDeadlinedEvent() {
		// TODO Auto-generated method stub

	}

	private void handleAddDurationEvent() {
		// TODO Auto-generated method stub

	}

	private void handleAddOneDayEvent() {
		System.out.print("  when: ");
		String dateString = kb.next();
		MyDate date = parseDateString(dateString);

		System.out.print("  title: ");
		String title = kb.next();

		OneDayEvent ev = new OneDayEvent(title, date);

		//		System.out.println(ev.toString());  // test
		
		addEvent(ev);
	}

	private void addEvent(Event ev) {
//		if (n >= capacity) {
//			reallocate();
//		}
		events.add(ev);
	}

//	private void reallocate() {
//		Event [] tmpArray = new Event [capacity*2];
//		for (int i=0; i<n; i++) {
//			tmpArray[i] = events.get(i);
//		}
//
//		events = tmpArray;
//		capacity *= 2;
//	}

	private MyDate parseDateString(String dateString) {
		String [] tokens = dateString.split("/");

		int year = Integer.parseInt(tokens[0]);
		int month = Integer.parseInt(tokens[1]);
		int day = Integer.parseInt(tokens[2]);

		MyDate d = new MyDate(year, month, day);

		return d;
	}

	public static void main(String[] args) {
		Scheduler app = new Scheduler();
		app.processCommand();
	}

}
