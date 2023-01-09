Feature: Registro de usuarios

  @Functional
  Scenario: Registrar un usuario
    Given ir a la página
    And  click en el botón 'Sign Up'
    And llenar el campo 'Estoyprobando456' y 'holaprueba123'
    When click en el botón 'Sign up' y 'Aceptar'
    Then click en el botón 'Close'
