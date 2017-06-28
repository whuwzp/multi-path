from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # initilaize topology   
        Topo.__init__( self )

        # add hosts and switches     
        s1 = self.addSwitch( 's1' )       
        s2 = self.addSwitch( 's2' )       
        s3 = self.addSwitch( 's3' )       
   
        s4 = self.addSwitch( 's4' )       
        s5 = self.addSwitch( 's5' )       

        h1 = self.addHost( 'h1' )       
        h2 = self.addHost( 'h2' )       





        # add links

        self.addLink(s4,s1  )
        self.addLink(s4,s2  )
        self.addLink(s4,s3  )

        self.addLink(s5,s1  )
        self.addLink(s5,s2  )
        self.addLink(s5,s3  )

        self.addLink(h1,s4  )
        self.addLink(h2,s5  )



topos = { 'mytopo': ( lambda: MyTopo() ) }
