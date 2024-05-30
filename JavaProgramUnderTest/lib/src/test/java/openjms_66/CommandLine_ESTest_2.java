package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_2 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("org.exolab.jms.util.CommandLine", "oz-cUYR,!mz7Y=");
      assertTrue(boolean0);
      
      String string0 = commandLine0.value("org.exolab.jms.util.CommandLine", "");
      assertEquals("oz-cUYR,!mz7Y=", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("#,N>W", "$~v?");
      String string0 = commandLine0.value("#,N>W");
      assertEquals("$~v?", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("o&Raizpn]rzxN", "o&Raizpn]rzxN");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("o&Raizpn]rzxN");
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
        commandLine0.add((String) null, "", false);
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
        commandLine0.add((String) null, "+_ >/KHY%j.CX+\".");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test10()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-<@RO^+:u)BUl :l";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("-<@RO^+:u)BUl :l", "uFb&vxiOj", false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("-<@RO^+:u)BUl :l", "-<@RO^+:u)BUl :l", true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", (String) null);
      boolean boolean1 = commandLine0.add("", (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      boolean boolean1 = commandLine0.add("", "org.exolab.jms.util.CommandLine", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[7];
      stringArray0[0] = "";
      stringArray0[1] = "-";
      stringArray0[2] = "-";
      stringArray0[3] = "v}$f;N3qL";
      stringArray0[4] = "-";
      stringArray0[5] = "";
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
  public void test14()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", (String) null);
      boolean boolean1 = commandLine0.add("", (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test15()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("", "");
      String string0 = commandLine0.value("", "");
      assertEquals("", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("azlfk]2~iu4K-v]L9", (String) null);
      assertNull(string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("", "", true);
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("o");
      assertNull(string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("-?AT7>iR??c=05");
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = new String[7];
      stringArray0[0] = "";
      stringArray0[1] = "v?";
      stringArray0[2] = "<@RO^+:u)BUl :l";
      stringArray0[3] = "";
      stringArray0[4] = "IXWHv}M`C!:pJO";
      stringArray0[5] = ")GtmLNTsMzK+";
      stringArray0[6] = "Z";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isParameter("");
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch("");
      assertFalse(boolean0);
  }
}
