package openjms_66;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CommandLine_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.value("k", (String) null);
      assertNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "-";
      stringArray0[4] = "";
      stringArray0[5] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("", "");
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String[] stringArray0 = new String[7];
      stringArray0[0] = "";
      stringArray0[1] = "";
      stringArray0[2] = "bfpG].gw@k{";
      stringArray0[3] = "-";
      stringArray0[4] = "s*FZn";
      stringArray0[5] = "+9s/Q:qa7kQW\"\"X";
      stringArray0[6] = "";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("");
      assertNotNull(string0);
      assertEquals("s*FZn", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "q+I";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      boolean boolean0 = commandLine0.add("q+I", (String) null, false);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isSwitch("q+I");
      assertTrue(boolean1 == boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("t", "t", true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.isParameter("t");
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
        commandLine0.add((String) null, "-E1)&8*s{Fd;", false);
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
        commandLine0.add((String) null, "c");
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
      commandLine0.add("", "", false);
      String string0 = commandLine0.value("");
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[5];
      stringArray0[0] = "";
      stringArray0[1] = "";
      stringArray0[2] = "";
      stringArray0[3] = "+o1Fh2}q/UnXg!d} Ki";
      stringArray0[4] = "BfZfcI8tsZ*";
      CommandLine commandLine0 = new CommandLine(stringArray0);
      String string0 = commandLine0.value("BfZfcI8tsZ*");
      assertNull(string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[7];
      stringArray0[0] = "";
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine(stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-";
      CommandLine commandLine0 = new CommandLine(stringArray0);
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[7];
      stringArray0[0] = "-";
      stringArray0[1] = "-";
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
      boolean boolean0 = commandLine0.add("5.U#UmP[q", "5.U#UmP[q");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.add("5.U#UmP[q", "5.U#UmP[q", true);
      assertTrue(boolean1);
  }

  @Test
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("$sKE$vB_@IslJW/z", "$sKE$vB_@IslJW/z");
      boolean boolean1 = commandLine0.add("$sKE$vB_@IslJW/z", "$sKE$vB_@IslJW/z", false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test18()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, false);
      boolean boolean1 = commandLine0.add((String) null, (String) null, false);
      assertFalse(boolean1 == boolean0);
      assertFalse(boolean1);
  }

  @Test
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null);
      boolean boolean1 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean1 == boolean0);
      assertTrue(boolean1);
  }

  @Test
  public void test20()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("6/=Gwy", "6/=Gwy");
      assertTrue(boolean0);
      
      String string0 = commandLine0.value("6/=Gwy", "T");
      assertEquals("6/=Gwy", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add("$sKE$vB_@IslJW/z", "$sKE$vB_@IslJW/z");
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists("$sKE$vB_@IslJW/z");
      assertTrue(boolean1);
  }

  @Test
  public void test22()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.exists("$sKE$vB_@IslJW/z");
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.add((String) null, (String) null, true);
      assertTrue(boolean0);
      
      boolean boolean1 = commandLine0.exists((String) null);
      assertTrue(boolean1);
  }

  @Test
  public void test24()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isParameter("-");
      assertFalse(boolean0);
  }

  @Test
  public void test25()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      boolean boolean0 = commandLine0.isSwitch((String) null);
      assertFalse(boolean0);
  }
}
