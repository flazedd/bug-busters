package openjms_66;
import java.util.Hashtable;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[]{"-option", "value", "-switch"});
    assertTrue(cmd.exists("option"));
}

@Test
public void testIsParameter() {
    CommandLine cmd = new CommandLine(new String[]{"-option", "value", "-switch"});
    assertTrue(cmd.isParameter("option"));
}

}