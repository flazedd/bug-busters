package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "");
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "5W\"ct9D`x=-l4*;");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("{/.eaNiP~};$7`@C]");
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.value((String) null, "=");
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
        commandLine0.add((String) null, "P.wDEF", true);
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
      boolean boolean0 = commandLine0.add("G$", "G$");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("G$", "", true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean1);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[1] = "1._+";
      stringArray0[0] = "-";
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "jJ[o";
      stringArray0[1] = "";
      stringArray0[2] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      boolean boolean1 = commandLine0.add("", "", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      stringArray0[2] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "JaDfaperk^!;HPU7Oc";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("JaDfaperk^!;HPU7Oc", (String) null);
      boolean boolean1 = commandLine0.add("JaDfaperk^!;HPU7Oc", (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "", false);
      String string0 = commandLine0.value("", (String) null);
      assertEquals("", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("k8Mw>i`;7SfNyV5zk", "|~`i)g.@KU-U4WCt}q");
      assertEquals("|~`i)g.@KU-U4WCt}q", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "jJ[o";
      stringArray0[1] = "";
      stringArray0[2] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("-", "jJ[o");
      String string0 = commandLine0.value("-");
      assertEquals("jJ[o", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("");
      assertNull(string0);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("-", "-");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("-");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "JaDfaperk^!;HPU7Oc";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.exists("JaDfaperk^!;HPU7Oc");
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "jJ[o";
      stringArray0[1] = "";
      stringArray0[2] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.exists("");
      assertTrue(boolean0);
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
      boolean boolean0 = commandLine0.isSwitch((String) null);
      assertFalse(boolean0);
  }
}
