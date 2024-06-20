package openjms_66;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import java.util.Hashtable;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testCommandLine() {
    String[] args = {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals(true, cmd.exists("option1"));
}
@Test
public void testCommandLineParameter() {
    String[] args = {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineSwitch() {
    String[] args = {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals(true, cmd.isSwitch("option2"));
}
@Test
public void testCommandLineAdd() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertEquals("defaultValue", cmd.value("option2", "defaultValue"));
}
@Test
public void testCommandLineExists() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option2", null);
    assertEquals(true, cmd.exists("option2"));
}
@Test
public void testCommandLineAddOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", true);
    assertEquals("value2", cmd.value("option1"));
}
@Test
public void testCommandLineAddNoOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", false);
    assertEquals("value1", cmd.value("option1"));
}
}