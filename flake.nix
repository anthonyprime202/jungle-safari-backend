{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let 
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [ 
        jq
        (python313.withPackages(ps: with ps; [
          fastapi 
          fastapi-cli 
          uvicorn
          sqlmodel
          psycopg2
          python-dotenv
          python-lsp-server
          fpdf
          num2words
          passlib
          python-jose
          cryptography
          pyjwt
          python-multipart
          bcrypt
        ]))];
    };
  };
}
