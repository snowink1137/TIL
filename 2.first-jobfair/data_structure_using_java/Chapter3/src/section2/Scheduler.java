package section2;

import java.util.*;

public class Scheduler {
	
	public Event events [] = new Event [100];
	public int n = 0;
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
				
			} else if (command.equals("show")) {
				
			} else if (command.equals("exit")) {
				break;
			} 
		}
		
		kb.close();
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
		
		System.out.println(ev.toString());  // test
		
		events[n++] = ev;
	}

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
