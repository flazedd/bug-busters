package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("NS)zbW,=", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-";
      stringArray0[1] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("-", "org.exolab.jms.util.CommandLine");
      assertEquals("org.exolab.jms.util.CommandLine", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[8];
      stringArray0[0] = ";|@M3SaUx+Fg)5]\t%";
      stringArray0[1] = "org.exolab.jms.util.CommandLine";
      stringArray0[2] = "akqB=";
      stringArray0[3] = " M=M*k9vxIw0uM{T`tZ";
      stringArray0[4] = "";
      stringArray0[5] = "V)z=";
      stringArray0[6] = "";
      stringArray0[7] = "hK6%c>~)IXF";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine");
      assertEquals("org.exolab.jms.util.CommandLine", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch((String) null);
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      String[] stringArray0 = new String[8];
      stringArray0[0] = "";
      stringArray0[1] = "7~=9#,";
      stringArray0[2] = "";
      stringArray0[3] = "#]|K5vs";
      stringArray0[4] = "";
      stringArray0[5] = "f>gTK2V!E(TBCR";
      stringArray0[6] = "";
      stringArray0[7] = "U=;Iv7<";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
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
        commandLine0.add((String) null, ";-4@iO[JFyUrO@eA", false);
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
        commandLine0.add((String) null, "W|k6Hfa");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test11()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-";
      stringArray0[1] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "", true);
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test13()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      boolean boolean1 = commandLine0.add("", "", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test14()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("p1w", "", true);
      String string0 = commandLine0.value("p1w");
      assertEquals("", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("", "");
      assertEquals("", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "");
      String string0 = commandLine0.value("", "");
      assertEquals("", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("");
      assertNull(string0);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("-B~uH(D:3=jJ(3 a51.g");
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test22()  throws Throwable  {
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
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("-B~uH(D:3=jJ(3 a51.g");
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
