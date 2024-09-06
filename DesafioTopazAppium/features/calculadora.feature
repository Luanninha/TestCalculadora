@tag1
Feature: Testar a funcionalidade de soma da calculadora

  Scenario: Somar dois números
    Given que a calculadora está aberta
    When eu digito o número 10
    And eu aperto o botão "+"
    And eu digito o número 20
    And eu aperto o botão "="
    Then o resultado deve ser 30