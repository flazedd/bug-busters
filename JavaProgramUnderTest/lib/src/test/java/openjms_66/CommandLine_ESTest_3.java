package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("^e~`k8Onzm9<@J/r", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = " @YqjPuz+m";
      stringArray0[4] = ".&tno";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("", " @YqjPuz+m", false);
      String string0 = commandLine0.value("");
      assertEquals(" @YqjPuz+m", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "!w>!<O-fg";
      stringArray0[1] = "Y";
      stringArray0[2] = "Y";
      stringArray0[3] = "-";
      stringArray0[4] = "-";
      stringArray0[5] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isSwitch("");
      assertTrue(boolean0);
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
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter(">o0fb!I=^r*<apmu");
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.value((String) null, "");
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
        commandLine0.exists((String) null);
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
        commandLine0.add((String) null, ">3o~h~kP=@?", false);
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
        commandLine0.add((String) null, "-");
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
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("", "org.exolab.jms.util.CommandLine", true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "", false);
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("^@2cz+#");
      assertNull(string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "!w>!<O-fg";
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "-Lx5J:";
      stringArray0[1] = ".";
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      boolean boolean1 = commandLine0.add("", "", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "");
      String string0 = commandLine0.value("", (String) null);
      assertEquals("", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("i", "i");
      assertEquals("i", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("org.exolab.jms.util.CommandLine");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("org.exolab.jms.util.CommandLine");
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test23()  throws Throwable  {
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
  public void test24()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("I.KljO5+<F:ZVp1oWPS");
      assertFalse(boolean0);
  }
}
