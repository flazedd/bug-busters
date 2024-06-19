package openjms_66;
import org.junit.jupiter.api.Test;
import java.util.Hashtable;
import java.util.Vector;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[] {"-a", "value", "-b", "-c", "anotherValue"});
    assertTrue(cmd.exists("a"));
    assertTrue(cmd.exists("b"));
    assertTrue(cmd.exists("c"));
    assertEquals("value", cmd.value("a"));
    assertEquals("anotherValue", cmd.value("c"));
    assertNull(cmd.value("b"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "oldValue");
    cmd.add("option", "newValue", true);
    assertEquals("newValue", cmd.value("option"));
}
@Test
public void testCommandLineNoOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "oldValue");
    cmd.add("option", "newValue", false);
    assertEquals("oldValue", cmd.value("option"));
}
@Test
public void testCommandLineIsParameter() {
    CommandLine cmd = new CommandLine(new String[] {"-a", "value", "-b", "-c", "anotherValue"});
    assertTrue(cmd.isParameter("a"));
    assertTrue(cmd.isParameter("c"));
    assertFalse(cmd.isParameter("b"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine cmd = new CommandLine(new String[] {"-a", "value", "-b", "-c", "anotherValue"});
    assertEquals("defaultValue", cmd.value("d", "defaultValue"));
}
@Test
public void testCommandLineEmptyArgs() {
    CommandLine cmd = new CommandLine(new String[] {});
    assertFalse(cmd.exists("a"));
    assertNull(cmd.value("a"));
}
@Test
public void testCommandLineConstructor() {
    CommandLine cmd = new CommandLine();
    assertFalse(cmd.exists("a"));
    assertNull(cmd.value("a"));
}
@Test
public void testCommandLineAddTwice() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "oldValue");
    cmd.add("option", "newValue", false);
    assertEquals("oldValue", cmd.value("option"));
    cmd.add("option", "newValue", true);
    assertEquals("newValue", cmd.value("option"));
}
}