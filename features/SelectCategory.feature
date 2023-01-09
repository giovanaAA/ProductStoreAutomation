Feature: Seleccionar categoria

  @Functional
  Scenario: Seleccionar categoría "Laptops"
    Given ir a la página
    And click en el botón 'Laptops'
    When click en el primer item
    Then click en el botón 'Add to cart'


