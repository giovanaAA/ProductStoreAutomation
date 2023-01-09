Feature: Inicio de sesión de usuarios
  Background: Registrar nuevo usuario
    Given ir a la página
    And  click en el botón 'Sign Up'
    And llenar el campo 'pruebaminombre' y 'hola12345678'
    And click en el botón 'Sign up' y 'Aceptar'
    And click en el botón 'Close'

  @Functional
  Scenario: Iniciar sesión
    Given ir a la página
    And  click en el botón 'Log in'
    When llenar 'pruebaminombre' y 'hola12345678'
    Then click en el botón de cierre 'Log in'