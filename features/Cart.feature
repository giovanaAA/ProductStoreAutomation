Feature: Añadir compra a carrito
  Background: Seleccionar item de la categoria laptop
    Given ir a la página
    And click en el botón 'Laptops'
    And click en el primer item
    And click en el botón 'Add to cart'

  @Functional
  Scenario: Añadir primer item al carrito
    Given click en la pestaña 'Cart'
    And click en el botón 'Place Order'
    And llenar el formulario de compra 'Jose', 'Bolivia', 'Tarija', '123456', 'Enero', '2023'
    When click en el botón 'Purchase'
    Then click en el botón 'Ok'
