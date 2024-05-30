package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      String string0 = commandLine0.value("", "gM,<38IJqw~1\"<9#L");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "8YRnA@q+> v>XpB");
      String string0 = commandLine0.value("");
      assertEquals("8YRnA@q+> v>XpB", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("auKQa^BC%", (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("auKQa^BC%");
      assertTrue(boolean1);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
      String[] stringArray0 = new String[4];
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.value(stringArray0[1], "K?");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
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
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.add((String) null, "TjF", true);
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
        commandLine0.add((String) null, "@eV2{E`^ANXT%.{i2U");
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
      boolean boolean0 = commandLine0.add("", "qfR_dPVfAiMjh");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("", "r!{qLpa?n%R1", true);
      assertTrue(boolean1);
  }

  @Test
  public void test10()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("auKQa^BC%", (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("auKQa^BC%", (String) null, true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "");
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "";
      stringArray0[1] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("ix:R");
      assertNull(string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("K", "K");
      boolean boolean1 = commandLine0.add("K", "K", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "-$28rHG]?I@:";
      stringArray0[1] = "-$28rHG]?I@:";
      stringArray0[2] = "?~-ij+6]SV0!";
      stringArray0[3] = "`x*#l{GzRsv8O=";
      stringArray0[4] = "-$28rHG]?I@:";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("-$28rHG]?I@:", "`x*#l{GzRsv8O=", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("-$28rHG]?I@:", "");
      assertTrue(boolean1);
  }

  @Test
  public void test15()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("WGKu)", "WGKu)");
      String string0 = commandLine0.value("WGKu)", "WGKu)");
      assertEquals("WGKu)", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-<$28rHG]?I@:";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("-<$28rHG]?I@:", (String) null);
      assertNull(string0);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "", false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("-:H0G");
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
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
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "";
      stringArray0[1] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "-$28rHG]?I@:";
      stringArray0[1] = "-$28rHG]?I@:";
      stringArray0[2] = "?~-ij+6]SV0!";
      stringArray0[3] = "`x*#l{GzRsv8O=";
      stringArray0[4] = "-$28rHG]?I@:";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isParameter("eKi`J~jZ6<e'5`");
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch((String) null);
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      String[] stringArray0 = new String[2];
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }
}
