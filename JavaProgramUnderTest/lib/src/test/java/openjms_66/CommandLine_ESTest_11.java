package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "N_4K,wK#n* ;0'k";
      stringArray0[1] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("r%<yh,mf7i.Evh=}", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "", false);
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "'&!**rIF,J- 7KS");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
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
        commandLine0.add((String) null, "y9PwVEkRHH=}Re{e=*");
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
      boolean boolean0 = commandLine0.add("}{/bl,qB,egTA,c,k", "}{/bl,qB,egTA,c,k", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("}{/bl,qB,egTA,c,k", "}{/bl,qB,egTA,c,k", true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("org.exolab.jms.util.CommandLine", (String) null, false);
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null);
      boolean boolean1 = commandLine0.add("", (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("W+0hsfQf]V!");
      assertNull(string0);
  }

  @Test
  public void test14()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("3!;F", "3!;F");
      boolean boolean1 = commandLine0.add("3!;F", "", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test15()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("q\"e'K", "");
      assertTrue(boolean0);
      
      String string0 = commandLine0.value("q\"e'K", "q\"e'K");
      assertEquals("", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("", "'&!**rIF,J- 7KS");
      String string0 = commandLine0.value("");
      assertEquals("'&!**rIF,J- 7KS", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "org.exolab.jms.util.CommandLine";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine", "org.exolab.jms.util.CommandLine");
      assertEquals("org.exolab.jms.util.CommandLine", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("!Xv[=G}Tlx7+^g", "!Xv[=G}Tlx7+^g");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("!Xv[=G}Tlx7+^g");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("!Xv[=G}Tlx7+^g");
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "--org.exolab.jms.util.CommandLine";
      stringArray0[1] = ",9b1$%P";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test24()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isParameter("");
      assertFalse(boolean0);
  }

  @Test
  public void test25()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "";
      stringArray0[1] = "I]r\n- ,`mY<B)F)Mu_";
      stringArray0[2] = "'&!**rIF,J- 7KS";
      stringArray0[3] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isSwitch("QP{");
      assertFalse(boolean0);
  }

  @Test
  public void test26()  throws Throwable  {
      String[] stringArray0 = new String[2];
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
}
