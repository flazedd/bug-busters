package openjms_66;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.Hashtable;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testCommandLine() {
    CommandLine commandLine = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertEquals(true, commandLine.isSwitch("option2"));
}
@Test
public void testCommandLineParameter() {
    CommandLine commandLine = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertEquals("value1", commandLine.value("option1"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine commandLine = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertEquals("defaultValue", commandLine.value("option3", "defaultValue"));
}
@Test
public void testCommandLineAddOption() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option", null);
    assertEquals(true, commandLine.isSwitch("option"));
}
@Test
public void testCommandLineAddParameter() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option", "value");
    assertEquals("value", commandLine.value("option"));
}
@Test
public void testCommandLineExists() {
    CommandLine commandLine = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertEquals(true, commandLine.exists("option1"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option", "value1");
    commandLine.add("option", "value2", true);
    assertEquals("value2", commandLine.value("option"));
}
@Test
public void testCommandLineNoOverwrite() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option", "value1");
    commandLine.add("option", "value2", false);
    assertEquals("value1", commandLine.value("option"));
}
}