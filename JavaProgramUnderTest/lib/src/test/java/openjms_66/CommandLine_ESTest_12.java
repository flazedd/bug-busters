package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("b", "");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "";
      stringArray0[1] = "X1fMuQaU_u";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = "6`|5[`/8)1D6>>8n'";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("", "ffqu5]_M|XO#N<y%O`%");
      String string0 = commandLine0.value("");
      assertEquals("ffqu5]_M|XO#N<y%O`%", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "5";
      stringArray0[1] = "?K_";
      stringArray0[2] = "cOe}Du{_aVQ";
      stringArray0[3] = "s9Z~8~B>t";
      stringArray0[4] = "org.exolab.jms.util.CommandLine";
      stringArray0[5] = "kU'eVM";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("-O~{jJpJX");
      assertFalse(boolean0);
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
        commandLine0.add((String) null, "", true);
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
        commandLine0.add((String) null, "");
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
      boolean boolean0 = commandLine0.add("-q@:zED5%m2OPVd", "I", false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("-q@:zED5%m2OPVd", "P7", true);
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
      commandLine0.add("", "");
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("C|2Dbd mK");
      assertNull(string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[8];
      stringArray0[0] = "\u0000=uK\"k";
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
      boolean boolean0 = commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      boolean boolean1 = commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-org.exolab.jms.util.CommandLine";
      stringArray0[1] = "-org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("-", "-");
      String string0 = commandLine0.value("-", "-");
      assertEquals("-", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("G.,Fkirzfc~a4K", (String) null);
      assertNull(string0);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("");
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test23()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-org.exolab.jms.util.CommandUine";
      stringArray0[1] = "e/uoqwaU{";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test24()  throws Throwable  {
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
  public void test25()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch((String) null);
      assertFalse(boolean0);
  }
}
