package saxpath_24;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Axis_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = Axis.lookup("ancestor-or-self");
      assertEquals(13, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = Axis.lookup("descendant-or-self");
      assertEquals(12, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = Axis.lookup("self");
      assertEquals(11, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Axis.lookup("namespace");
      assertEquals(10, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = Axis.lookup("attribute");
      assertEquals(9, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = Axis.lookup("preceding");
      assertEquals(8, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = Axis.lookup("following");
      assertEquals(7, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = Axis.lookup("preceding-sibling");
      assertEquals(6, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = Axis.lookup("following-sibling");
      assertEquals(5, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = Axis.lookup("ancestor");
      assertEquals(4, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = Axis.lookup("parent");
      assertEquals(3, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = Axis.lookup("descendant");
      assertEquals(2, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = Axis.lookup("child");
      assertEquals(1, int0);
  }

  @Test
  public void test13()  throws Throwable  {
      int int0 = Axis.lookup("MVL`:Ycgi2Qp6Djlfdh");
      assertEquals(0, int0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = Axis.lookup(13);
      assertEquals("ancestor-or-self", string0);
      assertNotNull(string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = Axis.lookup(12);
      assertNotNull(string0);
      assertEquals("descendant-or-self", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = Axis.lookup(11);
      assertEquals("self", string0);
      assertNotNull(string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = Axis.lookup(10);
      assertNotNull(string0);
      assertEquals("namespace", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Axis.lookup(9);
      assertNotNull(string0);
      assertEquals("attribute", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Axis.lookup(8);
      assertNotNull(string0);
      assertEquals("preceding", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Axis.lookup(7);
      assertEquals("following", string0);
      assertNotNull(string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Axis.lookup(6);
      assertNotNull(string0);
      assertEquals("preceding-sibling", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Axis.lookup(5);
      assertEquals("following-sibling", string0);
      assertNotNull(string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Axis.lookup(4);
      assertEquals("ancestor", string0);
      assertNotNull(string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Axis.lookup(3);
      assertNotNull(string0);
      assertEquals("parent", string0);
  }

  @Test
  public void test25()  throws Throwable  {
      String string0 = Axis.lookup(2);
      assertEquals("descendant", string0);
      assertNotNull(string0);
  }

  @Test
  public void test26()  throws Throwable  {
      String string0 = Axis.lookup(4619);
      assertNull(string0);
  }

  @Test
  public void test27()  throws Throwable  {
      String string0 = Axis.lookup(1);
      assertEquals("child", string0);
      assertNotNull(string0);
  }

  @Test
  public void test28()  throws Throwable  {
      Axis axis0 = new Axis();
      assertEquals(4, Axis.ANCESTOR);
  }
}
