package sfmis_7;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__6 {
@Test
public void base64EncodingDecodingTest() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64AltEncodingDecodingTest() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EmptyStringTest() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64NullInputTest() {
    try {
        Base64.base64ToByteArray(null);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // Expected exception
    }
}
@Test
public void base64InvalidInputTest() {
    try {
        Base64.base64ToByteArray("Invalid Base64 string");
        fail("Expected IllegalArgumentException for invalid input");
    } catch (IllegalArgumentException e) {
        // Expected exception
    }
}
@Test
public void base64MultipleEqualsTest() {
    String originalString = "Hello";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    base64String += "=="; // Add extra '=' characters
    try {
        Base64.base64ToByteArray(base64String);
        fail("Expected IllegalArgumentException for input with extra '=' characters");
    } catch (IllegalArgumentException e) {
        // Expected exception
    }
}
@Test
public void base64StringWithSpacesTest() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    String base64StringWithSpaces = base64String.replace("", " "); // Add spaces to the base64 string
    try {
        Base64.base64ToByteArray(base64StringWithSpaces);
        fail("Expected IllegalArgumentException for input with spaces");
    } catch (IllegalArgumentException e) {
        // Expected exception
    }
}
@Test
public void base64StringWithNonBase64CharactersTest() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    String base64StringWithNonBase64Characters = base64String + "!"; // Add a non-base64 character to the base64 string
    try {
        Base64.base64ToByteArray(base64StringWithNonBase64Characters);
        fail("Expected IllegalArgumentException for input with non-base64 characters");
    } catch (IllegalArgumentException e) {
        // Expected exception
    }
}
}