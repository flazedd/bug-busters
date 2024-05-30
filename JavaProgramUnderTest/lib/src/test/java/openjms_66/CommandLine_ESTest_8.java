package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("LE?i%g-M=MP)T30-L", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "";
      stringArray0[1] = "pI*r'Z=[j3";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("WWw*zrcgI", "");
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("org.exolab.jms.util.CommandLine", "", true);
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test05()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      // Undeclared exception!
      try { 
        commandLine0.value((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test06()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      // Undeclared exception!
      try { 
        commandLine0.value((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test07()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.isParameter((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test08()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.exists((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test09()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.add((String) null, "--org.exolab.jms.util.CommandLine", true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test10()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.add((String) null, "*`");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test11()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("org.exolab.jms.util.CommandLine", "", true);
      assertTrue(boolean1);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add((String) null, (String) null, true);
      boolean boolean1 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine");
      assertEquals("org.exolab.jms.util.CommandLine", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[8];
      stringArray0[0] = "-";
      stringArray0[1] = "h;jw+AI8oG&";
      stringArray0[2] = "-";
      stringArray0[3] = "E]do 4]9|T[_";
      stringArray0[4] = "";
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test15()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("---:", "---:");
      boolean boolean1 = commandLine0.add("---:", "---:", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add((String) null, (String) null, true);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-63p%_z6I6N";
      stringArray0[1] = "-63p%_z6I6N";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("6tr7jAh.kk/T'C2(n", "6tr7jAh.kk/T'C2(n");
      assertEquals("6tr7jAh.kk/T'C2(n", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      stringArray0[2] = "P_1ad h||k";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("", "");
      assertEquals("P_1ad h||k", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("6tr7jAh.kk/T'C2(n");
      assertNull(string0);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("");
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isParameter("-Y2yn>*h");
      assertFalse(boolean0);
  }

  @Test
  public void test25()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isSwitch("-w");
      assertFalse(boolean0);
  }
}
