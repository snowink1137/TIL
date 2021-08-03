package section3;

import java.io.*;
import java.util.*;

public class Code23 {
	static String [] words = new String [100000];
	static int [] count = new int [100000];
	static int n = 0;	
	
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		
		while (true) {
			System.out.print("$ ");
			String command = kb.next();
			
			if (command.equals("read")) {
				String filename = kb.next();
				makeIndex(filename);				
			} else if (command.equals("find")) {
				String str = kb.next();
				int index = findWord(str);
				if (index > -1) {
					System.out.println("The word " + words[index] + " appears " + count[index] + " times.");
				} else {
					System.out.println("The word " + str + " does not appear.");
				}
			} else if (command.equals("saveas")) {
				String fileName = kb.next();
				saveAs(fileName);
				
			} else if (command.equals("exit")) {
				break;
			}
			
			
		}
		
		kb.close();
		
// check¿ë ÄÚµå
//		for (int i=0; i<n; i++) {
//			System.out.println(words[i] + " " + count[i]);
//		}
		
	}
	
	static void makeIndex(String filename){
		try {
			Scanner inFile = new Scanner(new File(filename));
			
			while (inFile.hasNext()) {
				String str = inFile.next();
				
				String trimmed = trimming(str);
				
				if (trimmed != null) {
					String t = trimmed.toLowerCase();
					
					addWord(t);
				}
				
			}
			
			inFile.close();
		} catch (FileNotFoundException e) {
			System.out.println("No file");
			return;
		}
	}
	
	static String trimming(String str) {
		int i = 0;
		int j = str.length() - 1;
		
		while (i < str.length() && !Character.isLetter(str.charAt(i))) {
			i++;
		}
		
		while (j >= 0 && !Character.isLetter(str.charAt(j))) {
			j--;
		}
		
		if (i <= j) {
			String trimmed = str.substring(i, j+1);
			
			return trimmed;
		} else {
			return null;
		}
		
	}

	static void addWord(String str) {
		int index = findWord(str);  // return -1 if not found
		if (index != -1) {
			count[index] += 1;
		} else {
			int i = n - 1;
			for (; i>=0 && words[i].compareToIgnoreCase(str)>0; i--) {
				words[i+1] = words[i];
				count[i+1] = count[i];
			}
						
			words[i+1] = str;
			count[i+1] = 1;
			n++;
		}
	}
	
	static int findWord(String str) {
		for (int i=0; i<n; i++) {
			if (words[i].equals(str)) {
				return i;
			}
		}
		
		return -1;
	}
	
	static void saveAs(String fileName) {
		try {
			PrintWriter outFile = new PrintWriter(new FileWriter(fileName));
			for (int i=0; i<n; i++) {
				outFile.println(words[i] + " " + count[i]);
			}
			
			outFile.close();
		} catch (IOException e) {
			System.out.println("Save failed");
		}
	}
}
