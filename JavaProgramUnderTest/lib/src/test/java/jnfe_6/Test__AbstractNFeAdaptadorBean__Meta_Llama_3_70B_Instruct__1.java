package jnfe_6;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__AbstractNFeAdaptadorBean__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testCalculaDV() {
    assertEquals(7, AbstractNFeAdaptadorBean.calculaDV("3525081300010700010057001000003550100002348"));
}

@Test
public void testCalculaDV2() {
    assertEquals(5, AbstractNFeAdaptadorBean.calculaDV("3525081300010700010057001000003550100002349"));
}



}