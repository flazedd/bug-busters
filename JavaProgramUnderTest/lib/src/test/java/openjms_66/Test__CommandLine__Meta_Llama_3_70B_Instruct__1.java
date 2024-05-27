package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
import java.util.Hashtable;
import org.junit.jupiter.api.Test;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testExists() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
}

@Test
public void testValue() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertEquals("value1", cmd.value("option1"));
}

@Test
public void testIsSwitch() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.isSwitch("option2"));
}

@Test
public void testAdd() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "value");
    assertTrue(cmd.exists("option"));
}

@Test
public void testDefaultValue() {
    CommandLine cmd = new CommandLine();
    assertEquals("default", cmd.value("option", "default"));
}

@Test
public void testIsParameter() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.isParameter("option1"));
}

@Test
public void testAddOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "oldValue");
    cmd.add("option", "newValue", true);
    assertEquals("newValue", cmd.value("option"));
}

@Test
public void testAddNoOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option", "oldValue");
    cmd.add("option", "newValue", false);
    assertEquals("oldValue", cmd.value("option"));
}



}