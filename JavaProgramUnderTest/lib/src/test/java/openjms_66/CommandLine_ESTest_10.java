package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      String[] stringArray0 = new String[0];
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("", "");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.add("1CGbC4<hg%BdzS~f", "9NR40.Rn.l^JV]", true);
      String string0 = commandLine0.value("1CGbC4<hg%BdzS~f");
      assertEquals("9NR40.Rn.l^JV]", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "|tj4?)4]M";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = ".@KS>DP%P#l";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("", "%V%&/}");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("");
      assertTrue(boolean1);
  }

  @Test
  public void test04()  throws Throwable  {
      String[] stringArray0 = new String[5];
      CommandLine commandLine0 = new CommandLine();
      // Undeclared exception!
      try { 
        commandLine0.value(stringArray0[0], stringArray0[0]);
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
        commandLine0.add((String) null, "i.b:fO", true);
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
        commandLine0.add((String) null, ":X&C");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test10()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "";
      stringArray0[1] = "zv.I\"2Dl";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = "";
      stringArray0[5] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("", "0H<&|", true);
      assertTrue(boolean1);
  }

  @Test
  public void test11()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "";
      stringArray0[1] = "zv.I\"2Dl";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = "";
      stringArray0[5] = "org.exolab.jms.util.CommandLine";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add("", "");
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("25G7bWKy");
      assertNull(string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "-";
      stringArray0[1] = "._py5u}XRI?";
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
      String[] stringArray0 = new String[3];
      stringArray0[0] = "-3^";
      stringArray0[1] = "-3^";
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
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "|tj4?)4]M";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = ".@KS>DP%P#l";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      boolean boolean1 = commandLine0.add("", ".@KS>DP%P#l", false);
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
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("i.b:fO", (String) null);
      boolean boolean1 = commandLine0.add("i.b:fO", (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = ",1\"=C3+";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      commandLine0.add(",1\"=C3+", ",1\"=C3+");
      String string0 = commandLine0.value(",1\"=C3+", ",1\"=C3+");
      assertEquals(",1\"=C3+", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("", (String) null);
      assertNull(string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "|tj4?)4]M";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = ".@KS>DP%P#l";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("", "");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("");
      assertTrue(boolean1);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "|tj4?)4]M";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = ".@KS>DP%P#l";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
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
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-oYW";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test24()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("i.b:fO");
      assertFalse(boolean0);
  }

  @Test
  public void test25()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "|tj4?)4]M";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "";
      stringArray0[4] = ".@KS>DP%P#l";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.isSwitch("");
      assertFalse(boolean0);
  }
}
