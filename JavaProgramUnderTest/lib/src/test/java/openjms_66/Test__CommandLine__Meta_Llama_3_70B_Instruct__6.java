package openjms_66;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.Hashtable;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testCommandLine() {
    String[] args = new String[] {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals(true, cmd.exists("option1"));
}
@Test
public void testCommandLineParameter() {
    String[] args = new String[] {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineSwitch() {
    String[] args = new String[] {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals(true, cmd.isSwitch("option2"));
}
@Test
public void testCommandLineDefaultValue() {
    String[] args = new String[] {"-option1", "value1", "-option2", "-option3", "value3"};
    CommandLine cmd = new CommandLine(args);
    assertEquals("defaultValue", cmd.value("option4", "defaultValue"));
}
@Test
public void testCommandLineAddOption() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", null);
    assertEquals(true, cmd.exists("option1"));
}
@Test
public void testCommandLineAddParameter() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineAddOptionWithoutOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", null);
    assertEquals(false, cmd.add("option1", null, false));
}
@Test
public void testCommandLineAddParameterWithoutOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertEquals(false, cmd.add("option1", "new_value1", false));
    assertEquals("value1", cmd.value("option1"));
}
}