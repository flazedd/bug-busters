package openjms_66;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import java.util.Hashtable;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.isSwitch("option2"));
}
@Test
public void testCommandLineParameter() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2", "value2"});
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertEquals("default", cmd.value("option3", "default"));
}
@Test
public void testCommandLineAdd() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertTrue(cmd.isParameter("option1"));
}
@Test
public void testCommandLineExists() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
}
@Test
public void testCommandLineNoArgs() {
    CommandLine cmd = new CommandLine(new String[] {});
    assertFalse(cmd.exists("option1"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", true);
    assertEquals("value2", cmd.value("option1"));
}
@Test
public void testCommandLineNoOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", false);
    assertEquals("value1", cmd.value("option1"));
}
}