package section5;

import java.util.*;

public class MyArrayList<E> {
	private static final int INIT_CAPACITY = 10;
	private E [] theData;
	private int size;
	private int capacity = INIT_CAPACITY;
	
	public MyArrayList() {
		theData = (E []) new Object [INIT_CAPACITY];
		size = 0;
	}
	
	public void add(int index, E anEntry) {
		if (index < 0 || index > size) {
			throw new ArrayIndexOutOfBoundsException();
		}
		
		if (size >= capacity) {
			reallocate();
		}
		
		for (int i=size-1; i>=index; i--) {
			theData[i+1] = theData[i];
		}
		
		theData[index] = anEntry;
		size++;
	}
	
	private void reallocate() {
		capacity *= 2;
		theData = Arrays.copyOf(theData, capacity);
	}

	public void add(E anEntry) {
		add(size, anEntry);
	}
	
	public int size() {
		return size;
	}
	
	public int indexOf(E anEntry) {
		for (int i=0; i<size; i++) {
			if (theData[i].equals(anEntry)) {  // ****
				return i;
			}
		}
		return -1;
	}
	
	public E get(int index) {
		if (index < 0 || index > size) {
			throw new ArrayIndexOutOfBoundsException();
		}
		
		return theData[index];
	}
	
	public E set(int index, E newValue) {
		if (index < 0 || index > size) {
			throw new ArrayIndexOutOfBoundsException();
		}
		
		E oldValue = theData[index];
		theData[index] = newValue;
		return oldValue;
	}
	
	public E remove(int index) {
		if (index < 0 || index > size) {
			throw new ArrayIndexOutOfBoundsException();
		}
		
		E returnValue = theData[index];
		
		for (int i=index+1; i<size; i++) {
			theData[i-1] = theData[i];
		}
		
		size--;
		
		return returnValue;
	}
	
	
}
