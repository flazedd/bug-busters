package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Hashtable;
import java.util.Arrays;
import java.util.Vector;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
    assertTrue(cmd.exists("option2"));
    assertEquals("value1", cmd.value("option1"));
    assertNull(cmd.value("option2"));
}

@Test
public void testCommandLineWithDefault() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertEquals("value1", cmd.value("option1", "defaultValue"));
    assertEquals("defaultValue", cmd.value("option3", "defaultValue"));
}

@Test
public void testCommandLineAdd() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option2", null);
    assertTrue(cmd.isParameter("option1"));
    assertTrue(cmd.isSwitch("option2"));
    assertEquals("value1", cmd.value("option1"));
    assertNull(cmd.value("option2"));
}

@Test
public void testCommandLineOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", true);
    assertEquals("value2", cmd.value("option1"));
    cmd.add("option1", "value3", false);
    assertEquals("value2", cmd.value("option1"));
}

@Test
public void testCommandLineEmpty() {
    CommandLine cmd = new CommandLine(new String[]{});
    assertFalse(cmd.exists("option1"));
    assertNull(cmd.value("option1"));
}

@Test
public void testCommandLineMultipleValues() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option1", "value2"});
    assertTrue(cmd.exists("option1"));
    assertEquals("value2", cmd.value("option1"));
}

@Test
public void testCommandLineMultipleCalls() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
    assertTrue(cmd.exists("option2"));
    assertEquals("value1", cmd.value("option1"));
    assertNull(cmd.value("option2"));
    assertTrue(cmd.exists("option1"));
    assertTrue(cmd.exists("option2"));
    assertEquals("value1", cmd.value("option1"));
    assertNull(cmd.value("option2"));
}

@Test
public void testCommandLineNullArgument() {
    try {
        CommandLine cmd = new CommandLine(null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}

}