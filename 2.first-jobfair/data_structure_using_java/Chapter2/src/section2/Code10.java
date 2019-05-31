package section2;

import java.io.*;
import java.util.*;

public class Code10 {

	public static void main(String[] args) {
		try {
			Scanner in = new Scanner(new File("data.txt"));
			int n = in.nextInt();
			
			OrthoPolygon thePolygon = new OrthoPolygon(n);
			for (int i=0; i<n; i++) {
				thePolygon.addVertex(in.nextInt(), in.nextInt());
			}
			
			MyPoint2 thePoint = new MyPoint2(in.nextInt(), in.nextInt());
			
			in.close();
			
			if (thePolygon.contains(thePoint)) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}
			
			
		} catch (FileNotFoundException e) {
			System.out.println("No data file exists.");
			System.exit(1);
		}
	}

}
