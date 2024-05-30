package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("Z", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "65'@&lr0%I^", false);
      assertTrue(boolean0);
      
      String string0 = commandLine0.value("", "");
      assertEquals("65'@&lr0%I^", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "|Fe3)(", false);
      String string0 = commandLine0.value("");
      assertEquals("|Fe3)(", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("0IS]`", "", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("0IS]`");
      assertTrue(boolean1);
  }

  @Test
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
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
        commandLine0.add((String) null, "_j8T|di>", false);
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
        commandLine0.add((String) null, "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("1^Kh^rF=M", (String) null, true);
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("", (String) null, true);
      assertTrue(boolean1);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "-", true);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("0IS]`", "", true);
      boolean boolean1 = commandLine0.add("0IS]`", "0IS]`", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null, false);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine", "");
      assertEquals("", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("0IS]`", "", true);
      String string0 = commandLine0.value("0IS]`");
      assertEquals("", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value(")Obps{Cp^mix");
      assertNull(string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add(";MVp+T", "", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists(";MVp+T");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.exists("-kMK]**10p");
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test23()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isParameter("0IS]`");
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "0IS]`";
      stringArray0[1] = "Oo";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isSwitch("dNNZ524DP>)Ypn");
      assertFalse(boolean0);
  }

  @Test
  public void test25()  throws Throwable  {
      String[] stringArray0 = new String[2];
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }
}
